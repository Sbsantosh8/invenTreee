const __vite__mapDeps=(i,m=__vite__mapDeps,d=(m.f||(m.f=["assets/ScheduledTasksTable-D3Q2ET0M.js","assets/vendor-9x6k4T-r.js","assets/index-Bd_yPD7D.js","assets/index-DbKhsUu2.css","assets/InvenTreeTable-KDc6oHjF.js","assets/DesktopAppView-D7dqNL6j.js","assets/ThemeContext-DRe09WSE.js","assets/ThemeContext-DcZSjbzQ.css","assets/navigation-BUwul1Ze.js","assets/UseForm-C7xHtQGh.js","assets/dayjs.min-DUmzidR_.js","assets/ApiIcon-BBFuOj6_.js","assets/ApiIcon-lqZLHWg1.css","assets/Instance-ZaRjKoLj.js","assets/ActionDropdown-DlGcqXhK.js"])))=>i.map(i=>d[i]);
import{c as u,e as p,A as d,L as v,_ as S}from"./index-Bd_yPD7D.js";import{r as n,ce as T,i as s,j as e,cp as D,m,f6 as w,s as E,d as F,bG as O,S as P,bB as C,bI as i}from"./vendor-9x6k4T-r.js";import{S as r}from"./ThemeContext-DRe09WSE.js";import{F as M}from"./FactCollection-Crs9BYnL.js";import{u as y}from"./UseInstance-Cb46b_w1.js";import{u as x,I as _}from"./InvenTreeTable-KDc6oHjF.js";import"./DesktopAppView-D7dqNL6j.js";import"./navigation-BUwul1Ze.js";import"./UseForm-C7xHtQGh.js";import"./dayjs.min-DUmzidR_.js";import"./ApiIcon-BBFuOj6_.js";import"./Instance-ZaRjKoLj.js";import"./ActionDropdown-DlGcqXhK.js";function B({onRecordsUpdated:t}){const a=x("tasks-failed"),o=u(),[c,h]=n.useState(""),[f,{open:j,close:b}]=T(!1),k=n.useMemo(()=>[{accessor:"func",title:s._({id:"Q3P/4s"}),sortable:!0,switchable:!1},{accessor:"pk",title:s._({id:"YgxM31"})},{accessor:"started",title:s._({id:"JEGlfK"}),sortable:!0,switchable:!1},{accessor:"stopped",title:s._({id:"NnvXp5"}),sortable:!0,switchable:!1},{accessor:"attempt_count",title:s._({id:"BCmibk"})}],[]);return e.jsxs(e.Fragment,{children:[e.jsx(D,{opened:f,size:"xl",position:"right",title:e.jsx(r,{children:s._({id:"7Jw/XW"})}),onClose:b,children:c.split(`
`).map((l,g)=>e.jsx(m,{size:"sm",children:l},`error-${g}`))}),e.jsx(_,{url:p(d.task_failed_list),tableState:a,columns:k,props:{enableBulkDelete:o.isStaff(),afterBulkDelete:t,enableSelection:!0,onRowClick:l=>{l.result?(h(l.result),j()):(w("failed-task"),E({id:"failed-task",title:s._({id:"6RoHXm"}),message:s._({id:"OFdRJT"}),color:"red",icon:e.jsx(F,{})}))}}})]})}function R({onRecordsUpdated:t}){const a=x("tasks-pending"),o=u(),c=n.useMemo(()=>[{accessor:"func",title:s._({id:"Q3P/4s"}),switchable:!1},{accessor:"task_id",title:s._({id:"YgxM31"})},{accessor:"name",title:s._({id:"6YtxFj"})},{accessor:"lock",title:s._({id:"d+F6q9"}),sortable:!0,switchable:!1},{accessor:"args",title:s._({id:"OgB1k4"})},{accessor:"kwargs",title:s._({id:"/n/HCO"})}],[]);return e.jsx(_,{url:p(d.task_pending_list),tableState:a,columns:c,props:{afterBulkDelete:t,enableBulkDelete:o.isStaff(),enableSelection:!0}})}const z=v(n.lazy(()=>S(()=>import("./ScheduledTasksTable-D3Q2ET0M.js"),__vite__mapDeps([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]))));function q(){const{instance:t,refreshInstance:a}=y({endpoint:d.task_overview,hasPrimaryKey:!1,refetchOnMount:!0,defaultValue:{},updateInterval:3e4});return e.jsxs(e.Fragment,{children:[(t==null?void 0:t.is_running)==!1&&e.jsx(O,{title:s._({id:"Oe/dvo"}),color:"red",children:e.jsx(m,{children:s._({id:"HkhyUV"})})}),e.jsxs(P,{gap:"xs",children:[e.jsx(M,{items:[{title:s._({id:"sOEpG4"}),value:t==null?void 0:t.pending_tasks},{title:s._({id:"8OiyFS"}),value:t==null?void 0:t.scheduled_tasks},{title:s._({id:"DJ8M4D"}),value:t==null?void 0:t.failed_tasks}]}),e.jsx(C,{}),e.jsxs(i,{defaultValue:"pending",children:[e.jsxs(i.Item,{value:"pending",children:[e.jsx(i.Control,{children:e.jsx(r,{size:"lg",children:s._({id:"sOEpG4"})})}),e.jsx(i.Panel,{children:e.jsx(R,{onRecordsUpdated:a})})]},"pending-tasks"),e.jsxs(i.Item,{value:"scheduled",children:[e.jsx(i.Control,{children:e.jsx(r,{size:"lg",children:s._({id:"8OiyFS"})})}),e.jsx(i.Panel,{children:e.jsx(z,{})})]},"scheduled-tasks"),e.jsxs(i.Item,{value:"failed",children:[e.jsx(i.Control,{children:e.jsx(r,{size:"lg",children:s._({id:"DJ8M4D"})})}),e.jsx(i.Panel,{children:e.jsx(B,{onRecordsUpdated:a})})]},"failed-tasks")]})]})]})}export{q as default};
