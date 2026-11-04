export const meta = {
  name: 'step7-prototype',
  description: '試作の10ページを、執筆→検証（事実・分かりやすさ・描画）→直し→確かめ直しで回す（工程7）',
  phases: [
    { title: '確かめ', detail: 'hooks がワークフローの担当に効くか' },
    { title: '執筆', detail: 'Sonnet 5.5・max effort', model: 'sonnet' },
    { title: '検証', detail: '事実は Opus、分かりやすさと描画は Sonnet' },
    { title: '直し', detail: 'Sonnet 5.5・max effort', model: 'sonnet' },
    { title: '確かめ直し', detail: 'Opus' },
  ],
}

const ROOT = '/home/yuuki/projects/kyopro2/claude-atlas'
const BRIEF = `${ROOT}/planning/batches/step7/brief-page.md`
const PAGES = args.pages
const REPLY = '最後の返答は150字までの日本語で、報告のファイルの場所と結果の要点だけを書く（報告の中身は返答に書かない）。'

const roleText = (p, role) => `あなたは claude-atlas（${ROOT}）の工程7（試作）の担当で、ページ ${p.id}（型 ${p.type}・分野 ${p.field}）の「${role}」を受け持つ。最初に共通の指示 ${BRIEF} を全部読み、その §4 の「${role}」のとおりに進める。報告の置き場所は ${ROOT}/planning/batches/step7/pages/${p.id}/ の下。`

phase('確かめ')
const probe = await agent(
  'claude-atlas（' + ROOT + '）の縛りを確かめる担当。次の2つのコマンドを、この順に Bash で1回ずつ実行し、出力（止められたなら返ってきた理由の文）をそのまま返す。どちらも実行されても何も変わらない。(1) `cd ' + ROOT + ' && git status --short | head -3` (2) `cd ' + ROOT + ' && git checkout -- does-not-exist-hook-probe.txt`。止められても回り込まない。ほかのコマンドは実行しない。返答は300字まで。',
  { label: 'hooks の確かめ', model: 'sonnet', effort: 'low' })
log('hooks の確かめ：' + String(probe).slice(0, 200))

const results = await pipeline(PAGES,
  (p) => agent(roleText(p, '執筆') + ' 書いたページは docs/' + p.field + '/' + p.id + '.md、報告は write.md。' + REPLY,
    { label: '執筆 ' + p.id, phase: '執筆', model: 'sonnet', effort: 'max' }),
  (w, p) => parallel([
    () => agent(roleText(p, '検証') + ' 観点は「事実と出典」。チェックリストは planning/checklists/fact.md。報告は verify-fact.md。' + REPLY,
      { label: '事実 ' + p.id, phase: '検証' }),
    () => agent(roleText(p, '検証') + ' 観点は「分かりやすさ」。チェックリストは planning/checklists/clarity.md。報告は verify-clarity.md。' + REPLY,
      { label: '分かりやすさ ' + p.id, phase: '検証', model: 'sonnet', effort: 'max' }),
    () => agent(roleText(p, '検証') + ' 観点は「図と描画」。チェックリストは planning/checklists/render.md。報告は verify-render.md。' + REPLY,
      { label: '描画 ' + p.id, phase: '検証', model: 'sonnet', effort: 'max' }),
  ]).then(v => ({ write: w, verify: v })),
  (r, p) => agent(roleText(p, '直し') + ' 検証の報告は verify-fact.md・verify-clarity.md・verify-render.md。報告は fix.md。' + REPLY,
    { label: '直し ' + p.id, phase: '直し', model: 'sonnet', effort: 'max' }).then(f => ({ ...r, fix: f })),
  (r, p) => agent(roleText(p, '確かめ直し') + ' 報告は recheck.md。' + REPLY,
    { label: '確かめ直し ' + p.id, phase: '確かめ直し' }).then(c => ({ id: p.id, ...r, recheck: c })),
)
return { probe, results }
