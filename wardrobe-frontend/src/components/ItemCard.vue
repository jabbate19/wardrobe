<template>
  <div class="card h-100">
    <img :src="'https://s3.csh.rit.edu/skyzwardrobe/' + item!.id" class="card-img-top" />
    <div class="card-body">
      <h5 class="card-title">{{ item!.name }}</h5>
    </div>
  </div>
</template>

<script lang="ts">
import { type Item } from '../models'
import { type PropType } from 'vue'
export default {
  props: {
    item: Object as PropType<Item>
  }
}
</script>
