import{j as i,e0 as u,r as o}from"./vendor-9x6k4T-r.js";import{p as l}from"./index-Bd_yPD7D.js";function m(){return{code:{},description:{},responsible:{icon:i.jsx(u,{})}}}function f(){const n=l(),[r,c]=o.useState(""),a=o.useMemo(()=>{const e=[],t=Object.values(n.status??{}).find(s=>s.status_class===r);return Object.values((t==null?void 0:t.values)??{}).forEach(s=>{e.push({value:s.key,display_name:s.label})}),e},[n,r]);return o.useMemo(()=>({reference_status:{onValueChange(e){c(e)}},logical_key:{field_type:"choice",choices:a},key:{},name:{},label:{},color:{},model:{}}),[a])}function y(){return{name:{},definition:{},symbol:{}}}function b(){return{order:{hidden:!0},reference:{},description:{},quantity:{},price:{},price_currency:{},notes:{},link:{}}}export{y as c,b as e,m as p,f as u};
