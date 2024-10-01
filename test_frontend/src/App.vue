<template>
  <div>
    <h2>Dynamic Form</h2>
    <form @submit.prevent="submitForm">
      <div v-for="key in allowedKeys" :key="key.id">
        <label>{{ key.key }}</label>
        <component :is="getInputType(key.input_type)" v-model="formData[key.key]"
          :placeholder="key.expected_values?.join(', ')" :multiple="key.input_type === 'select_multiple'">
          <option v-if="key.input_type === 'select' && key.expected_values[0]" v-for="value in key.expected_values"
            :key="value" :value="value">{{
              value }}</option>
        </component>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const allowedKeys = ref([]);
    const formData = ref({});

    const fetchAllowedKeys = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/allowed-keys/'); // Adjust the URL as needed
        allowedKeys.value = response.data;
        allowedKeys.value.forEach(key => {
          formData.value[key.key] = key.expected_values ? key.expected_values[0] : ''; // Set default values
        });
      } catch (error) {
        console.error('Error fetching allowed keys:', error);
      }
    };

    const getInputType = (inputType) => {
      switch (inputType) {
        case 'text':
          return 'input';
        case 'number':
          return 'input';
        case 'select':
          return 'select';
        case 'select_multiple':
          return 'select';
        case 'textarea':
          return 'textarea';
        default:
          return 'input';
      }
    };

    const submitForm = async () => {
      try {
        const response = await axios.post('http://localhost:8000/api/submit-form/', formData.value); // Adjust the URL as needed
        console.log('Form submitted successfully:', response.data);
      } catch (error) {
        console.error('Error submitting form:', error);
      }
    };

    // Fetch allowed keys when the component is created
    fetchAllowedKeys();

    return {
      allowedKeys,
      formData,
      getInputType,
      submitForm,
    };
  },
};
</script>
