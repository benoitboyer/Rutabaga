import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home.vue";
// import Article from "@/views/Article.vue"
import Feed from "@/views/Feed.vue";
import RegisterFeed from "@/views/RegisterFeed.vue"


Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
	{
	    path: "/",
	    name: "home",
	    component: Home
	},
	{
	    path: "/feed/register/",
	    name: "feed-register",
	    component: RegisterFeed
	},
	{
	    path: "/feed/:id/",
	    name: "feed-detail",
	    component: Feed,
	    props: true
	}

    ]
});
