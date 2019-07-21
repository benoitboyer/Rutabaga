<template>
  <div class="register-feed">

    <div class="container">
      <form  @submit.prevent="validateForm">
        <h3 class="mb-4">Add a new RSS Feed to follow!</h3>
	<div v-if="error" class="alert alert-danger my-4" role="alert">
	  {{ error }}
	</div>
	<input v-model="feed.title" type="text" class="form-control form-control-lg mb-2" id="title" placeholder="Feed title">
	
	<input  v-model="feed.feed_url" type="text" class="form-control form-control-lg mb-2" id="feed-url" placeholder="Feed URL">
	<input  v-model="feed.website_url" type="text" class="form-control form-control-lg mb-3" id="website-url" placeholder="Website URL">
	<div class="form-group form-check">
	  <input  v-model="feed.favorite" type="checkbox" class="form-check-input" id="favorite">
	  <label class="form-check-label" for="favorite">Add to favorite</label>
	</div>
	<button type="submit" class="btn btn-outline-info">Register the Feed</button>
      </form>
      
    </div>
  </div>
</template>
<script>
export default {
    name: "RegisterFeed",
    data () {
	return {
	    error: null,
	    success: null,
	    feed: {
		title: null,
		feed_url: null,
		website_url: null,
		favorite: true
	    }
	}
    },
    methods: {
	validateForm() {
	    if(!this.feed.title || !this.feed_url || !website_url) {
		this.error = "All the fields are mandatory!"
	    } else if (this.feed_url){}
	    
	    
	}
    },
    
}
</script>
<style scoped>
form {
  color: #999;
}

</style>
