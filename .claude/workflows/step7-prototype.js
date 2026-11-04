export const meta = {
  name: 'step7-prototype',
  description: '試作のページを、執筆→分かりやすさの検証→直し（どれも Sonnet 5.5・max effort）で回す（工程7）',
  phases: [
    { title: '執筆', detail: 'Sonnet 5.5・max effort', model: 'sonnet' },
    { title: '検証', detail: '分かりやすさ（Sonnet 5.5・max effort）', model: 'sonnet' },
    { title: '直し', detail: 'Sonnet 5.5・max effort', model: 'sonnet' },
  ],
}

// v2（2026-11-04）：材料の束を読む。事実と出典の検証と確かめ直しを置かない（decisions.md 2026-11-04）
const ROOT = '/home/yuuki/projects/kyopro2/claude-atlas'
const BRIEF = `${ROOT}/planning/batches/step7/brief-page.md`
const PAGES = args.pages
const OPTS = { model: 'sonnet', effort: 'max' }
const REPLY = '最後の返答は100字までの日本語で、報告のファイルの場所と結果の要点だけを書く（報告の中身は返答に書かない）。'

const roleText = (p, role) => `あなたは claude-atlas（${ROOT}）の工程7（試作）の担当で、ページ ${p.id}（型 ${p.type}・分野 ${p.field}）の「${role}」を受け持つ。最初に共通の指示 ${BRIEF} を全部読み、そのとおりに進める（読むのは §2 の3つのファイルだけ。材料の束は ${ROOT}/state/packets/${p.id}.md）。報告の置き場所は ${ROOT}/planning/batches/step7/pages/${p.id}/ の下。`

const results = await pipeline(PAGES,
  (p) => agent(roleText(p, '執筆') + ' 書いたページは docs/' + p.field + '/' + p.id + '.md、報告は write.md。' + REPLY,
    { ...OPTS, label: '執筆 ' + p.id, phase: '執筆' }),
  (w, p) => agent(roleText(p, '分かりやすさの検証') + ' 報告は verify-clarity.md。' + REPLY,
    { ...OPTS, label: '検証 ' + p.id, phase: '検証' }).then(v => ({ write: w, verify: v })),
  (r, p) => agent(roleText(p, '直し') + ' 検証の報告は verify-clarity.md。報告は fix.md。' + REPLY,
    { ...OPTS, label: '直し ' + p.id, phase: '直し' }).then(f => ({ id: p.id, ...r, fix: f })),
)
return { results }
