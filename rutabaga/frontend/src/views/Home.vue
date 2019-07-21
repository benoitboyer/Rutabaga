<template>
  <div class="home">
    <div class="container mt-2">
      <div class="feed"
	  v-for="feed in feeds"
	  :key="feed.pk">
	<h2 class="text-center">
	  <router-link
	      :to="{ name: 'feed-detail', params: { id: feed.id } }"
	      class="feed-link"
	  >{{ feed.title }}
	  </router-link>
	</h2>
	<ArticlePreviewComponent
	    v-for="(article, index) in feed.contents"
	    :key="index"
	    :article="article"
	/>
      </div>
    </div>
    <div class="my-4">
      <p v-show="loadingFeeds">...loading...</p>
      <button
	  @click="getFeeds"
	  class="btn btn-sm btn-outline-success"
	  v-show="next">
	Load More
      </button>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
import ArticlePreviewComponent from "@/components/ArticlePreview.vue"
export default {
    name: "home",
    components: {
	ArticlePreviewComponent
    },
    data() {
	return {
	    feeds: [],
	    next: null,
	    loadingFeeds: false
	}
    },
    methods: {
	getFeeds() {
	    // make a GET Request to the questions list endpoint and populate the questions array
	    let endpoint = "/api/feeds/";
	    if (this.next) {
		endpoint =this.next
	    }
	    this.loadingFeeds = true;
	    apiService(endpoint)
		.then(data => {
		    this.feeds.push(...data.results)
		    this.loadingFeeds = false;
		    if (data.next) {
			this.next = data.next;
		    } else {
			this.next = null;
		    }
		})
	}
    },
    created() {
	this.getFeeds()
	document.title = "Rutabaga";
    }
};

</script>
<style>
.container {
  margin: 20px, 0px !important; 
}
</style>
