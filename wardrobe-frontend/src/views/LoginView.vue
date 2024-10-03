<template>
  <div class="container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" v-model="username" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" v-model="password" class="form-control" required />
      </div>
      <button type="submit" class="btn btn-primary">Log In</button>
    </form>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
      // Send login request to Flask backend
      let formData = new FormData()
      formData.append('username', this.username)
      formData.append('password', this.password)
      fetch('/api/login', {
        method: 'POST',
        body: formData
      }).then((response) => {
        if (response.ok) {
          this.$router.push('/')
        } else {
          alert('Invalid credentials')
        }
      })
    }
  }
}
</script>
