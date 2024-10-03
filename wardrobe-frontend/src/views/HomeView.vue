<script setup lang="ts">
import ItemCard from '../components/ItemCard.vue'
import UploadModal from '../components/UploadModal.vue'
</script>

<template>
  <div class="container">
    <h2>Your Wardrobe</h2>
    <button class="btn btn-primary mb-3" data-bs-toggle="modal" data-bs-target="#createItemModal">
      Add New Item
    </button>
    <div class="row" v-for="group in groupedItems">
      <div v-for="item in group" class="col-md-3 mb-3">
        <ItemCard :item="item" />
      </div>
    </div>
    <UploadModal />
  </div>
</template>

<script lang="ts">
import { type Item } from '../models'
import { computed } from 'vue'
export default {
  data() {
    const items = [] as Item[];
    return {
      items
    }
  },
  computed: {
    groupedItems() {
      return this.items.reduce(
        (r: any, e: any, i) => (i % 4 ? r[r.length - 1].push(e) : r.push([e])) && r,
        []
      )
    }
  },
  methods: {
    fetchItems() {
      fetch('/api/items')
        .then((response) => response.json())
        .then((data) => {
          this.items = data
        })
    }
  },
  created() {
    this.fetchItems()
  }
}
</script>
