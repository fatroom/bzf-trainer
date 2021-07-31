<template>
  <div class="question">
    <h1>{{ question.text }}</h1>
    <ol type="A">
      <li v-for="answer of question.answers" :class="answerClass(answer.id)" :key="answer.id"
          @click="validateAnswer(answer)">
        {{ answer.text }}
      </li>
    </ol>
  </div>
</template>

<script>
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}

export default {
  props: {
    question: {
      required: true,
      type: Object
    },
  },
  setup(props) {
    shuffleArray(props.question.answers)
  },
  data() {
    return {
      selectedAnswer: undefined,
    }
  },
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
    }
  }
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
