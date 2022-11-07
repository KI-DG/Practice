<template>
  <div >
    <input
      type="text"
      v-model.trim="todoTitle"  
      @keyup.enter="createTodo" >
      <!-- 좌우공백 없앤다 -->
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      // console.log(this.todoTitle)
      if (this.todoTitle) {
        // 공백이 아니라면
      this.$store.dispatch('createTodo', this.todoTitle)
      this.todoTitle= null
      }
    }
  },
  components: {
  }
}
</script>

<style>

</style>
