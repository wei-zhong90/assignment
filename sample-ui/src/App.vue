<template>
  <div>
    <div>
      <textarea v-model="text" placeholder="TO BE PROCESSED TEXT" rows="6" cols="150"></textarea>
    </div>
    <button v-on:click="processText">Process</button>
    <div>
      <p>{{ responseText }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      text: '',
      responseText: ''
    }
  },
  methods: {
    processText() {
      const xhr = new XMLHttpRequest()
      const url = process.env.VUE_APP_URL
      console.log(url)
      xhr.open('PUT', url, true)
      const that = this
      xhr.onreadystatechange = function() { 
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
          const response = JSON.parse(xhr.responseText)
          console.log(response.output)
          that.responseText = response.output
        }
      }
      xhr.send(this.text)
    }
  }
}
</script>
