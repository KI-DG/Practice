<template>
  <div v-if="video" style="margin-top: 30px">
    <iframe
      :src="`https://www.youtube.com/embed/${video.id.videoId}`"
      frameborder="0"
    ></iframe>
    <div>
      <h4>{{ video.snippet.title }}</h4>
      <hr />
      <p>{{ video.snippet.description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainVideo",
  props: {
    video: Object,
  },
};
</script>

<style>
</style>