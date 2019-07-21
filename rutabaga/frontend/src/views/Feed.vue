<template>
  <div class="feed">
    <div class="container mt-2">
      <div class="feed"
	<h2 class="text-center">
	  {{ feed.title }}
	  
	</h2>
	<ArticlePreviewComponent
	    v-for="(article, index) in feed.contents"
	    :key="index"
	    :article="article"
	/>
      </div>
    </div>
  </div>
</template>
<script>
import { apiService } from "@/common/api.service.js"
import ArticlePreviewComponent from "@/components/ArticlePreview.vue"
export default {
    name: "feed",
    components: {
	ArticlePreviewComponent
    },
    props: {
	id: {
	    type: Number,
	    required: true
	}
    },
    data() {
	return {
	    feed: {}
	}
    },
    methods: {
	getFeeds() {
	    // make a GET Request to the questions list endpoint and populate the questions array
	    let endpoint = `/api/feeds/${this.id}/`;
	    apiService(endpoint)
		.then(data => {
		    this.feed = data
		})
	}
    },
    created() {
	this.getFeeds()
	document.title = "Rutabaga";
    },
    
    beforeRouteUpdate(to, from, next) {
	    let endpoint = `/api/feeds/${to.params.id}/`;
	    apiService(endpoint)
		.then(data => {
		    this.feed = data
		})
	    return next()
    }
}
</script>
