<script>
export default {
  props: ["user_name", "content"]
};
</script>

<template>
  <div class="py-3">
    <div class="flex flex-col w-1/3 border-2 p-2 rounded-xl border-slate-800">
      <span class="text-2xl">{{ user_name }}</span>
      <span class="text-lg">{{ content }}</span>
    </div>
  </div>
</template>
