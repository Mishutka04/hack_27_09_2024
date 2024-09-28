import arrowSVG from '@assets/arrow-up.svg';
import botSVG from '@assets/bot-icon.svg';
import userSVG from '@assets/user-icon.svg';
import voiceSVG from '@assets/voice-fill.svg';

import './ChatBot.style.css';
import './ChatBotSubmit.style.css';

import { useState, useCallback, useRef } from 'react';
import { AnswerRating } from './AnswerRating/AnswerRating';
import { VoiceEnter } from './VoiceEnter/VoiceEnter';
import { TextEnter } from './TextEnter/TextEnter';

async function sendAPICall(messagesRef, setMessages, text) {
  const newMessages = [...messagesRef.current, { text: text, sender: 'user' }];
  setMessages(newMessages);
  try {
    const response = await fetch('http://192.144.12.86:8000/api/model/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question: text }),
    });

    const data = await response.json();

    setMessages([...newMessages, { text: data.answer, sender: 'bot' }]);
  } catch (error) {
    console.error('Ошибка при отправке сообщения:', error);
    setMessages([
      ...newMessages,
      { text: 'Ошибка: не удалось получить ответ от сервера', sender: 'bot' },
    ]);
  }
}

export const ChatBot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isListening, setIsListening] = useState(false);

  const messagesRef = useRef(messages);

  // eslint-disable-next-line react-hooks/exhaustive-deps
  const updateMessages = (newMessages) => {
    setMessages(newMessages);
    messagesRef.current = newMessages;
  };

  const sendMessage = useCallback(
    async (speechText = false) => {
      if (input.trim() !== '') {
        sendAPICall(messagesRef, updateMessages, input);
        setInput('');
      } else if (speechText) {
        sendAPICall(messagesRef, updateMessages, speechText);
      }
    },
    [input, updateMessages]
  );

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') sendMessage();
  };

  return (
    <div className="chat-bot">
      <div className="chat-bot__messages">
        {messages.map((msg, index) => (
          <div key={index} className="chat-bot__message__wrapper">
            <div
              className={`chat-message ${
                msg.sender === 'user' ? 'user-message' : 'bot-message'
              }`}
            >
              <div className={`${msg.sender === 'user' ? 'user' : 'bot'}-icon`}>
                {msg.sender === 'bot' ? (
                  <img src={botSVG} alt="bot" />
                ) : (
                  <img src={userSVG} alt="user" />
                )}
              </div>
              <p>{msg.text}</p>
              {msg.sender === 'bot' && <AnswerRating />}
            </div>
          </div>
        ))}
      </div>

      <div className="chat-bot__form">
        <input
          className={`chat-bot__input ${isListening ? 'listening' : ''}`}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          type="text"
          placeholder="Введите сообщение"
          readOnly={isListening}
        />
        <VoiceEnter
          setInput={setInput}
          setIsListening={setIsListening}
          sendMessage={sendMessage}
          source={voiceSVG}
        />
        <TextEnter 
          onclick={sendMessage} 
          source={arrowSVG} 
        />
      </div>
    </div>
  );
};