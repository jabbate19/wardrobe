<template>
    <button type="button" class="btn btn-danger" @click="deleteItem">Delete</button>
</template>

<script lang="ts">
import { useItemStore } from '@/stores/ItemStore';

export default {
    props: {
        id: String,
    },
    methods: {
        async deleteItem() {
            const response = await fetch(`/api/items/${this.id!}`, {
                method: 'DELETE',
            })

            if (!response.ok) {
                throw new Error('Network response was not ok')
            }

            const itemStore = useItemStore()
            itemStore.items.splice(itemStore.items.findIndex((item) => item.id === this.id, 1))
        }
    }
}
</script>