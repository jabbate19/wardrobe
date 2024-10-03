import { defineStore } from 'pinia';
import { type Item } from '@/models';

export const useItemStore = defineStore('items', {
  state: () => ({
    items: [] as Item[],
  }),
});
