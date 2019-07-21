<template>
  <div id="app">
    <div class="wrapper">
      <!-- Sidebar -->
      <SideBarComponent
	  :favoriteFeeds="favoriteFeeds"
      />

      <div id="content">
	<NavbarComponent/>
	<router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
import NavbarComponent from "@/components/NavBar.vue";
import SideBarComponent from "@/components/SideBar.vue"
export default {
    name: "App",
    data() {
	return {
	    favoriteFeeds: []
	}
    },
    components: {
	NavbarComponent,
	SideBarComponent
    },
    methods: {
        getFavorites() {
            // make a GET Request to the questions list endpoint and populate the questions array
	    let endpoint = "/api/feeds/";
	    apiService(endpoint)
		.then(data => {
		    this.favoriteFeeds.push(...data.results)
		})
        }
    },
    created() {
	this.getFavorites();
    }
};
</script>

<style>
@import "https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700";
body {
  font-family: 'Poppins', sans-serif;
  background: #fafafa;
}

p {
  font-family: 'Poppins', sans-serif;
  font-size: 1.1em;
  font-weight: 300;
  line-height: 1.7em;
  color: #999;
}

.line {
  width: 100%;
  height: 1px;
  border-bottom: 1px dashed #ddd;
  margin: 40px 0;
}


.navbar {
  padding: 15px 10px;
  background: #fff;
  border: none;
  border-radius: 0;
  margin-bottom: 40px;
  box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
}

.navbar-btn {
  box-shadow: none;
  outline: none !important;
  border: none;
}



/* ---------------------------------------------------
   CONTENT STYLE
   ----------------------------------------------------- */

#content {
  width: calc(100% - 250px);
  padding: 40px;
  min-height: 100vh;
  transition: all 0.3s;
  position: absolute;
  top: 0;
  right: 0;
}

#content.active {
  width: 100%;
}

/* ---------------------------------------------------
   MEDIAQUERIES
   ----------------------------------------------------- */

@media (max-width: 768px) {
  #sidebar {
    margin-left: -250px;
  }
  #sidebar.active {
    margin-left: 0;
  }
  #content {
    width: 100%;
  }
  #content.active {
    width: calc(100% - 250px);
  }
  #sidebarCollapse span {
    display: none;
  }
}
</style>
