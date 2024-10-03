import { defineStore } from 'pinia'
import { type Item } from '@/models'

export const useItemStore = defineStore('items', {
  state: () => ({
    items: [] as Item[],
    filters: [] as string[]
  }),
  getters: {
    filteredItems: (state) => {
      if (state.filters.length == 0) {
        return state.items
      }
      return state.items.filter(
        (item) => item.tags.filter((tag) => state.filters.includes(tag)).length == state.filters.length
      )
    },
    groupedFilteredItems: (state) => {
      if (state.filters.length == 0) {
        return state.items.reduce(
          (r: any, e: any, i) => (i % 4 ? r[r.length - 1].push(e) : r.push([e])) && r,
          []
        )
      }
      return state.items
        .filter((item) => item.tags.filter((tag) => state.filters.includes(tag)).length == state.filters.length)
        .reduce((r: any, e: any, i) => (i % 4 ? r[r.length - 1].push(e) : r.push([e])) && r, [])
    }
  }
})
