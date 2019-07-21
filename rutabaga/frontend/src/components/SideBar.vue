<template>
  <nav id="sidebar">
    <div class="sidebar-header">
      <a href="/">
	<h3>Rutabaga</h3>
      </a>
    </div>

    <ul class="list-unstyled components">
      <p>RSS the smart way</p>
      <button
      </button>
      <li>
        <a href="#" class="sidebarCollapse">
	  <i class="fas fa-align-left"></i> Read Mode</a>
      </li>
     
      
      <li class="active">
        <a href="#homeSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle"><i class="fas fa-star"></i> My Favorite Feeds</a>
        <ul class="collapse list-unstyled" id="homeSubmenu">
          
	  <li v-for="favorite in favoriteFeeds">
	    <router-link
		:to="{ name: 'feed-detail', params: { id: favorite.id } }"
		class="feed-link"
	    >{{ favorite.title }}
	    </router-link>
          </li>
        </ul>
      </li>
      <li>
	<router-link
	    :to="{ name: 'feed-register' }"
	>
	  <i class="fas fa-plus"></i> New Feed
	</router-link>
      </li>
      <li>
        <a href="#"><i class="fas fa-cog"></i> Manage My Feeds</a>
      </li>
      <li>
        <a href="/accounts/logout/"><i class="fas fa-sign-out-alt"></i> Logout</a>
      </li>
    </ul>
  </nav>
</template>
<script>
export default {
    name: "SideBarComponent",
    props: {
	favoriteFeeds: {
	    type: Array,
	    required: true
	}
    }
};
</script>
<style>
/* ---------------------------------------------------
   SIDEBAR STYLE
   ----------------------------------------------------- */

.wrapper {
  display: flex;
  width: 100%;
}

#sidebar {
  width: 250px;
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  z-index: 999;
  background: #7386D5;
  color: #fff;
  transition: all 0.3s;
}

#sidebar a,
#sidebar a:hover,
#sidebar a:focus {
  color: inherit;
  text-decoration: none;
  transition: all 0.3s;
}

#sidebar.active {
  margin-left: -250px;
}

#sidebar-collapse-btn:hover {
  border: solid 1px #fff;
  border-radius : .25rem;
  background-color:#6d7fcc;
  color: #fff;
  font-weight: 400;
  padding: .375rem .75rem;
  font-size: 1rem;
  line-height: 1.5;
}

#sidebar .sidebar-header {
  padding: 20px;
  background: #6d7fcc;
}

#sidebar ul.components {
  padding: 20px 0;
  border-bottom: 1px solid #47748b;
}

#sidebar ul p {
  color: #fff;
  padding: 10px;
}

#sidebar ul li a {
  padding: 10px;
  font-size: 1.1em;
  display: block;
}

#sidebar ul li a:hover {
  color: #7386D5;
  background: #fff;
}

#sidebar ul li.active>a,
a[aria-expanded="true"] {
  color: #fff;
  background: #6d7fcc;
}

a[data-toggle="collapse"] {
  position: relative;
}

.dropdown-toggle::after {
  display: block;
  position: absolute;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
}

ul ul a {
  font-size: 0.9em !important;
  padding-left: 30px !important;
  background: #6d7fcc;
}

ul.CTAs {
  padding: 20px;
}

ul.CTAs a {
  text-align: center;
  font-size: 0.9em !important;
  display: block;
  border-radius: 5px;
  margin-bottom: 5px;
}

a.download {
  background: #fff;
  color: #7386D5;
}

a.article,
a.article:hover {
  background: #6d7fcc !important;
  color: #fff !important;
}

</style>
