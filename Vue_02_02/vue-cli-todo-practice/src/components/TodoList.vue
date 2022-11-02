<template>
  <div>
    <ul v-for="(todo, index) in todos" :key="index">
      <!-- 키가 있어야 됨 -->
      <TodoListItem :todo="todo" @delete-todo="deleteTodo" />
    </ul>
  </div>
</template>

<script>
import TodoListItem from "@/components/TodoListItem";
export default {
  name: "TodoList",
  components: {
    TodoListItem,
  },
  props: {
    todos: Array,
  },
  methods: {
    deleteTodo: function (todo) {
      this.$emit("delete-todo", todo);
    },
  },
};
</script>

<style>
</style>