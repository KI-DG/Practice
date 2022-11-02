<template>
  <div id="app">
    <TodoList :todos="todos" @delete-todo="deleteTodo" />
    <TodoForm @create-todo="createTodo" />
  </div>
</template>

<script>
import TodoForm from "@/components/TodoForm";
import TodoList from "@/components/TodoList";

export default {
  name: "App",
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      todos: [],
    };
  },
  methods: {
    createTodo: function (todoTitle) {
      const todo = {
        title: todoTitle,
      };
      this.todos.push(todo);
    },
    deleteTodo: function (todo) {
      // 인덱스 번호를 알아야 된다
      const index = this.todos.indexOf(todo);
      // 인덱스를 지우고 다시 todos를 만드는 것
      this.todos.splice(index, 1);
    },
  },
};
</script>

<style>
</style>
