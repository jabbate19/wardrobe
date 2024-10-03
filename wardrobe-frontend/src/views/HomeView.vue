<script setup lang="ts">
import ItemCard from '../components/ItemCard.vue'
import UploadModal from '../components/UploadModal.vue'
</script>

<template>
  <div class="container">
    <h2>Your Wardrobe</h2>
    <h3>{{ itemStore.filteredItems.length }} Items</h3>
    <button class="btn btn-primary mb-3" data-bs-toggle="modal" data-bs-target="#createItemModal">
      Add New Item
    </button>
    <button class="btn btn-primary mb-3" @click="showFilters = !showFilters">Filter</button>
    <ItemFilter v-if="showFilters" />
    <div class="row" v-for="group in itemStore.groupedFilteredItems">
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
import { useItemStore } from '../stores/ItemStore'
import ItemFilter from '@/components/ItemFilter.vue'
export default {
  data() {
    const itemStore = useItemStore()
    const showFilters = false
    return {
      itemStore,
      showFilters
    }
  },
  computed: {
    groupedItems() {
      return this.itemStore.filteredItems.reduce(
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
          this.itemStore.items = data
        })
    }
  },
  created() {
    this.fetchItems()
  }
}
</script>
