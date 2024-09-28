import { FaqMenuItem } from '@components/FaqMenuItem/FaqMenuItem'

import './FaqMenu.style.css';

export const FaqMenu = () => {
  return (
    <div className='main__wrapper__content__faq-menu-container'>
        <ul className='faq-menu__pen-tabs'> 
            <FaqMenuItem text={'Нейросеть ответит на ваши вопросы!'} isActive={true}/>
        </ul>
    </div>
  )
}
