export const meta = {
  name: 'step8-wave',
  description: '第一波のページを、執筆（Sonnet 5.5・high）→分かりやすさの検証と直し（Sonnet 5.5・medium）の2段で回す（工程8）',
  phases: [
    { title: '執筆', detail: 'Sonnet 5.5・high effort', model: 'sonnet' },
    { title: '検証と直し', detail: '分かりやすさの検証と直し（Sonnet 5.5・medium effort）', model: 'sonnet' },
  ],
}

// v3.1（2026-11-05）：工程7の step7-prototype.js を写し、工程8の置き場所（planning/batches/step8/）にした。2段（執筆／検証と直し）。読むのは束と執筆カードだけ。検査は tools/check_page.py で2回
const ROOT = '/home/yuuki/projects/kyopro2/claude-atlas'
const BRIEF = `${ROOT}/planning/batches/step8/brief-page.md`
const PAGES = args.pages
const WRITE_OPTS = { model: 'sonnet', effort: 'high' }
const REVIEW_OPTS = { model: 'sonnet', effort: 'medium' }
const REPLY = '最後の返答は100字までの日本語で、報告のファイルの場所と結果の要点だけを書く（報告の中身は返答に書かない）。ただし、報告のファイルの Write が道具に止められたら、回り込まず（Bash などで書かず）、報告の中身を最後の返答に書く（このときは100字の決まりより優先する）。'

const roleText = (p, role) => `あなたは claude-atlas（${ROOT}）の工程8（第一波）の担当で、ページ ${p.id}（型 ${p.type}・分野 ${p.field}）の「${role}」を受け持つ。最初に共通の指示 ${BRIEF} を全部読み、そのとおりに進める。読むのは材料の束 ${ROOT}/state/packets/${p.id}.md と執筆カード ${ROOT}/planning/guides/card.md だけ。ページは1回の Write で書き、検査は \`uv run python tools/check_page.py ${p.id}\` を書き終えた後と直した後の2回だけ流す。Web の取得は3回まで。報告の置き場所は ${ROOT}/planning/batches/step8/pages/${p.id}/ の下。` + (p.note ? ` このページだけの追加の指示：${p.note}` : '')

const results = await pipeline(PAGES,
  (p) => agent(roleText(p, '執筆') + ' 書いたページは docs/' + p.field + '/' + p.id + '.md、報告は write.md。' + REPLY,
    { ...WRITE_OPTS, label: '執筆 ' + p.id, phase: '執筆' }),
  (w, p) => agent(roleText(p, '分かりやすさの検証と直し（書いた本人とは別の担当）') + ' 書かれたページは docs/' + p.field + '/' + p.id + '.md、執筆の報告は write.md、あなたの報告は review.md。' + REPLY,
    { ...REVIEW_OPTS, label: '検証と直し ' + p.id, phase: '検証と直し' }).then(r => ({ id: p.id, write: w, review: r })),
)
return { results }
