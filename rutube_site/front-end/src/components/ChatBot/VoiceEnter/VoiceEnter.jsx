import { useRef } from 'react';

// eslint-disable-next-line react/prop-types
export const VoiceEnter = ({ source, sendMessage, setIsListening }) => {
  const recognitionRef = useRef(null);
  
  if (!recognitionRef.current) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      console.error('SpeechRecognition API не поддерживается вашим браузером');
      return null;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = 'ru-RU';
    recognition.interimResults = true;

    recognition.onresult = (event) => {
      const result = event.results[event.resultIndex];
      if (result.isFinal) {
        const transcript = result[0].transcript;
        sendMessage(transcript); 
        setIsListening(false); 
      }
    };

    recognition.onerror = (event) => {
      console.error('SpeechRecognition error:', event.error);
      setIsListening(false); 
    };

    recognition.onend = () => {
      setIsListening(false);
    };

    recognitionRef.current = recognition;
  }

  const startListening = () => {
    setIsListening(true);
    recognitionRef.current.start();
  };

  const stopListening = () => {
    recognitionRef.current.stop();
    setIsListening(false);
  };

  return (
    <button
      className="chat-bot__submit"
      onMouseDown={startListening}
      onMouseUp={stopListening}
      onTouchStart={startListening}
      onTouchEnd={stopListening}
    >
      <img src={source} className="chat-bot__submit__icon" alt="voice" />
    </button>
  );
};
