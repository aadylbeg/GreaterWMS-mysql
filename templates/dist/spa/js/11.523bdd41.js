(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[11],{"7c2e":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t._self._c;return e("q-page",{directives:[{name:"show",rawName:"v-show",value:!t.fab,expression:"!fab"}],staticClass:"flex flex-center"},[e("div",{staticStyle:{"margin-top":"-7%"}},[e("div",{staticStyle:{color:"#4C5875","text-align":"center"},attrs:{className:"q-mb-xl"}},[e("div",{staticStyle:{"font-weight":"bold","font-size":"50px","letter-spacing":"10px"}},[t._v("WELCOME")]),e("div",{staticStyle:{"font-size":"18px","letter-spacing":"2px"}},[t._v("\n        GreaterWMS\n        "),t.isEnglish?e("span",[t._v(" ")]):t._e(),t._v("\n        "+t._s(t.$t("index.index_title"))+"\n      ")])]),e("div",{staticClass:"flex flex-center"},[e("lottie-web-cimo",{ref:"lottie_web",staticStyle:{width:"60%","max-width":"80%"}})],1)]),e("div",{staticStyle:{position:"absolute",right:"2%",bottom:"8%","font-family":"SourceHanSansCN","font-size":"16px",color:"#4C5875"}},[t._v("——\n       Easy Come   Easy Go    ——\n  ")])])},i=[],s=a("3c55"),o=a("a0ba"),l=a("0967"),c=a("18d6"),r={name:"PageIndexMobile",components:{LottieWebCimo:s["a"]},data(){return{isEnglish:!1,cleardata:[],height:"",width:"100%"}},methods:{},beforeCreate:function(){l["b"].is.cordova&&navigator.splashscreen.show()},computed:{fab:{get(){return this.$store.state.fabchange.fab}}},created:function(){c["a"].set("menulink",""),"en-us"===this.$q.localStorage.getItem("lang")?this.isEnglish=!0:this.isEnglish=!1},beforeMount:function(){l["b"].is.cordova&&window.setTimeout((function(){navigator.splashscreen.hide()}),-1e3)},mounted:function(){var t=this,e=o["a"].getInstance().get().test;e.toArray().then((a=>{a.length>0?(t.cleardata=[],e.each((e=>{t.cleardata.push(e.id)})),e.bulkDelete(this.cleardata),t.cleardata=[]):e.add({id:1,test:"next"})}))}},d=r,h=a("42e1"),f=a("9989"),u=a("eebe"),g=a.n(u),p=Object(h["a"])(d,n,i,!1,null,null,null);e["default"]=p.exports;g()(p,"components",{QPage:f["a"]})}}]);