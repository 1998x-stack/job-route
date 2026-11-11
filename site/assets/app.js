(() => {
  "use strict";
  const input=document.querySelector("#route-search");
  const chips=[...document.querySelectorAll("[data-filter]")];
  const cards=[...document.querySelectorAll("[data-card]")];
  const count=document.querySelector("#result-count");
  const empty=document.querySelector("#no-results");
  if(!input || !count || !empty)return;
  let category="all";
  function normalize(x){return String(x).toLocaleLowerCase("zh-CN").normalize("NFKC").trim()}
  function update(){
    const q=normalize(input.value);
    let visible=0;
    for(const card of cards){
      const matches=(category==="all"||card.dataset.category===category)&&normalize(card.dataset.search).includes(q);
      card.hidden=!matches;
      if(matches) visible++;
    }
    count.textContent="显示 "+visible+" / "+cards.length+" 条路线";
    empty.hidden=visible!==0;
  }
  input.addEventListener("input",update);
  for(const chip of chips)chip.addEventListener("click",()=>{
    category=chip.dataset.filter;
    for(const c of chips){const isActive=c===chip;c.classList.toggle("active",isActive);c.setAttribute("aria-pressed",String(isActive))}
    update();
  });
  document.addEventListener("keydown",(event)=>{
    if(event.key==="/"&&!event.ctrlKey&&!event.metaKey&&!event.altKey&&document.activeElement!==input&&!["INPUT","TEXTAREA"].includes(document.activeElement?.tagName)){
      event.preventDefault(); input.focus();
    }
    if(event.key==="Escape"&&document.activeElement===input){input.value="";update();input.blur()}
  });
  update();
})();
