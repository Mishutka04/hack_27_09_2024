import { ChatBot } from '@components/ChatBot/ChatBot';
import { FaqMenu } from '../FaqMenu/FaqMenu';

import './MainContent.style.css';

export const MainContent = () => {

  return (
    <div className='main__wrapper'>
      <div className="main__wrapper__content">
        <FaqMenu />
        <h1 className='main__wrapper__header'>Задайте нейросети интересующий вас вопрос</h1>
        <ChatBot />
      </div>
    </div>
  )
}
