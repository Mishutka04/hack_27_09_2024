import { useState } from 'react';
import './CodeEnter.style.css';

export const CodeEnter = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  
  const openModal = () => {
    setIsModalOpen(true);
  }

  const closeModal = () => {
    setIsModalOpen(false);
  } 

  return (
    <div className='code-enter'>
        <h2>Получайте точные ответы быстрее с нашим чат-ботом <span className='light-blue-font'>RUTUBE</span> и телеграмм ботом!</h2>

        <p className='code-enter__text'>Мы рады предложить вам еще более умный и эффективный способ получать ответы на ваши вопросы. Синхронизируйте свой телеграмм с нашим ботом и сайтом RUTUBE, чтобы улучшить свой опыт использования и достичь новых уровней удобства!</p>

        <h3>Почему это <span className='light-blue-font'>важно</span> для вас:</h3>
        <ul>
          <li><span className='light-blue-font'>Точные и персонализированные ответы</span> – бот будет запоминать ваши предыдущие запросы и предлагать более точные и релевантные ответы.</li>
          <li><span className='light-blue-font'>Мгновенные уведомления</span> – больше не нужно ждать или проверять вручную. Получайте нотификации прямо в Telegram, как только бот ответит на ваш вопрос.</li>
          <li><span className='light-blue-font'>Постоянное улучшение</span> – ваши взаимодействия помогают улучшить не только бота, но и всю технологию RUTUBE, чтобы каждый ваш запрос обрабатывался еще быстрее и точнее.</li>
        </ul>
        
        <p className='code-enter__text'>Введите <span className='light-blue-font' onClick={openModal}>коDick</span></p>

        {isModalOpen && 
            <>
                <div className="backdrop" onClick={closeModal}></div>
                <div className="modal">
                    Привет! Введи код, молю!!!
                </div>
            </>
        }
    </div>
  )
}