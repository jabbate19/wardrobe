<template>
  <div>
    <div v-for="tag in tags" :key="tag">
      <input
        type="checkbox"
        :id="tag"
        :value="tag"
        v-model="itemStore.filters"
      />
      <label :for="tag">{{ tag }}</label>
    </div>
  </div>
</template>

<script>
import { useItemStore } from '@/stores/ItemStore'

export default {
  data() {
    const itemStore = useItemStore()
    return {
      tags: [],
      itemStore
    }
  },
  methods: {
    fetchTags() {
      fetch('/api/tags')
        .then((response) => response.json())
        .then((data) => {
          this.tags = data
        })
        .catch((error) => {
          console.error('Error fetching tags:', error)
        })
    }
  },
  mounted() {
    this.fetchTags()
  }
}
</script>
