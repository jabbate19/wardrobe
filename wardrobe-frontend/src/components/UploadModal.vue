<template>
  <div
    class="modal fade"
    id="createItemModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="createItemModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="createItemModalLabel">Add New Item</h5>
          <button
            id="createItemModalClose"
            type="button"
            class="close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitForm">
            <div class="form-group">
              <label for="name">Name</label>
              <input type="text" class="form-control" v-model="name" required />
            </div>
            <div class="form-group">
              <label for="image">Image File</label>
              <input
                type="file"
                class="form-control-file"
                @change="handleFileUpload"
                accept="image/*"
                required
              />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { useItemStore } from '../stores/ItemStore'
export default {
  data() {
    return {
      name: '',
      imageFile: null
    }
  },
  methods: {
    closeModal() {
      document.getElementById('createItemModalClose')!.click()
    },
    handleFileUpload(event: any) {
      this.imageFile = event.target.files[0]
    },
    async submitForm() {
      const formData = new FormData()
      formData.append('name', this.name)
      formData.append('image', this.imageFile!)

      try {
        const response = await fetch('/api/items', {
          method: 'POST',
          body: formData
        })

        if (!response.ok) {
          throw new Error('Network response was not ok')
        }

        const data = await response.json()
        const itemStore = useItemStore()
        itemStore.items.push(data)
        this.closeModal() // Hide modal on success
      } catch (error) {
        console.error('Error:', error)
      }
    }
  }
}
</script>
