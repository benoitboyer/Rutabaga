<template>
  <div class="article">
    <div class="card mt-4">
      <div class="card-header">
	<h3>
	  <a :href="article.link">{{ article.title }}</a>
	</h3>
      </div>
      <div class="card-body">
	<p v-html="article.summary.substring(0,350)+' ...'"></p>
        <br/>
        <button class="btn btn-outline-info">Read More</button>
      </div>
      <div class="card-footer">
	<p>Author: {{ article.author_detail.name }}</p>
	<p>{{ article.published }}</p>
      </div>
    </div>
  </div>
  
</template>
<script>
export default {
    name: "ArticlePreviewComponent",
    props: {
	article: {
	    type: Object,
	    required: true
	}
    }
} 
</script>
