<template>
  <div class="question">
    <h1>{{ question.text }}</h1>
    <img v-if="question.img" alt="Question illustration" :src="question.img">
    <ol type="A">
      <li v-for="answer of question.answers" :class="answerClass(answer.id)" :key="answer.id"
          @click="validateAnswer(answer)">
        {{ answer.text }}
      </li>
    </ol>
    <button @click="selectedAnswer = undefined; $emit('next-question')">Next</button>
  </div>
</template>

<script>

export default {
  props: {
    question: {
      required: true,
      type: Object
    },
  },
  data() {
    return {
      selectedAnswer: undefined,
    }
  },
  emits: ['next-question'],
  methods: {
    validateAnswer(answer) {
      this.selectedAnswer = answer
    },
    answerClass(answerId) {
      if (this.selectedAnswer && answerId === this.selectedAnswer.id) {
        if (this.selectedAnswer.correct) {
          return 'correct'
        } else {
          return 'incorrect'
        }
      }
    },
  },
}
</script>

<style scoped>
li.correct {
  background: green;
}

li.incorrect {
  background: red;
}

</style>
