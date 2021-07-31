<template>
  <Question :question=currentQuestion @next-question="selectNextQuestion()"></Question>
</template>

<script>
import Question from './components/Question.vue'
import {ref} from 'vue'
import questions from '../public/data/bzf.json'

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

export default {
  name: 'App',
  components: {
    Question
  },

  setup() {
    shuffleArray(questions);
    let questionsRef = ref(questions)

    return {
      questions: questionsRef
    }
  },
  data() {
    return {
      currentQuestionIdx: 0
    }
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentQuestionIdx]
    }
  },
  methods: {
    selectNextQuestion() {
      this.currentQuestionIdx++;
      if (this.currentQuestionIdx === this.questions.length) {
        this.currentQuestionIdx = 0;
      }
      shuffleArray(this.questions[this.currentQuestionIdx].answers);
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
