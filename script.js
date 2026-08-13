// Minimal client: fetch data/skills.json and render
fetch('/data/skills.json').then(r=>r.json()).then(skills=>{
  const container = document.getElementById('skills')||document.getElementById('results')
  if(!container) return
  if(Array.isArray(skills)){
    skills.forEach(s=>{
      const el = document.createElement('div')
      el.innerHTML = `<strong>${s.name}</strong> — ${s.purpose} <span style="color:#666">(${s.category})</span>`
      container.appendChild(el)
    })
  }
})

// Simple search for search.html
const q = document.getElementById('q')
if(q){
  q.addEventListener('input', async ()=>{
    const idx = await fetch('/website/search-index.json').then(r=>r.json())
    const qv = q.value.toLowerCase()
    const out = idx.filter(i=> i.name.toLowerCase().includes(qv) || i.purpose.toLowerCase().includes(qv) || i.category.toLowerCase().includes(qv))
    const results = document.getElementById('results')
    results.innerHTML = ''
    out.forEach(o=>{
      const li = document.createElement('li')
      li.textContent = `${o.name} — ${o.purpose} (${o.category})`
      results.appendChild(li)
    })
  })
}
