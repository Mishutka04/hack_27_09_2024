import './AnswerRating.style.css';

import { useState } from "react";

export const AnswerRating = () => {
  const [response, setResponse] = useState(null);

  const handleVote = (isPositive) => {
    setResponse(isPositive ? 'yes' : 'no');
  }

  return (
    <div className="rating-area">
      {!response ? ( // Если ответа нет, показываем блок с вопросом
        <div className="vote-answer">
          <p>Вам помог ответ?</p>
          <button className='vote-answer__btn blue-btn-active agree-btn' onClick={() => handleVote(true)}>Да</button>
          <button className='vote-answer__btn blue-btn-active disagree-btn' onClick={() => handleVote(false)}>Нет</button>
        </div>
      ) : response === 'yes' ? ( // Если ответ "Да"
        <p>Спасибо за ваш отзыв!</p>
      ) : ( // Если ответ "Нет"
        <p>Переводим вас на живого специалиста...</p>
      )}
    </div>
  )
}