import axios from 'axios'

const getAPI = axios.create({
  baseURL: 'http://172.17.0.2:5000',
  timeout: 0
})

export default async function get_chatbot_response(client_input: object) {
  const response = await getAPI.post('/messages', client_input)
  return response.data
}
