import{j as s,C as h,l as _,S as n,i as e,bB as d,J as j,G as u,m as f,f2 as p,v as g,n as c}from"./vendor-9x6k4T-r.js";import{e as S,L as P,S as m,a as b}from"./ThemeContext-DRe09WSE.js";import{c as A,a as C,e as E,A as I}from"./index-Bd_yPD7D.js";import{ProtectedRoute as y}from"./Layout-B6kb79Gg.js";import{u as z}from"./use-form-Cwc3m1M6.js";import"./links-BvcwiLHd.js";import"./navigation-BUwul1Ze.js";import"./DesktopAppView-D7dqNL6j.js";import"./UseInstanceName-DvvSLbUj.js";import"./Instance-ZaRjKoLj.js";import"./ApiIcon-BBFuOj6_.js";function V(){const i=z({initialValues:{new_password1:"",new_password2:""}}),a=A(),w=S();function o(r){let t=(r==null?void 0:r.new_password2)||(r==null?void 0:r.new_password1)||(r==null?void 0:r.error)||e._({id:"KEnIWF"});Array.isArray(t)||(t=[t]),t.forEach(x=>{c.show({title:e._({id:"SlfejT"}),message:x,color:"red"})})}function l(){C.post(E(I.user_change_password),{new_password1:i.values.new_password1,new_password2:i.values.new_password2}).then(r=>{r.status===200?(c.show({title:e._({id:"IrZaAn"}),message:e._({id:"+p8fKY"}),color:"green",autoClose:!1}),w("/login")):o(r.data)}).catch(r=>{o(r.response.data)})}return s.jsx(P,{children:s.jsx(y,{children:s.jsx(h,{mih:"100vh",children:s.jsx(_,{w:"md",miw:425,children:s.jsxs(n,{children:[s.jsx(m,{size:"xl",children:e._({id:"KbS2K9"})}),s.jsx(d,{}),a.username()&&s.jsx(j,{children:s.jsxs(u,{children:[s.jsx(m,{size:"md",children:e._({id:"7PzzBU"})}),s.jsx(f,{children:a.username()})]})}),s.jsx(d,{}),s.jsxs(n,{gap:"xs",children:[s.jsx(p,{required:!0,"aria-label":"input-password-1",label:e._({id:"7vhWI8"}),description:e._({id:"0StR7t"}),...i.getInputProps("new_password1")}),s.jsx(p,{required:!0,"aria-label":"input-password-2",label:e._({id:"yjkELF"}),description:e._({id:"479pdJ"}),...i.getInputProps("new_password2")})]}),s.jsx(g,{type:"submit",onClick:l,children:s.jsx(b,{id:"7VpPHA"})})]})})})})})}export{V as default};
