import { useState } from 'react';
import './Account.style.css';

// Сделать форму для ввода кода
// Авторизация / Верификация
// Лайк / дизлайк

export const Account = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const openModal = () => {
    setIsModalOpen(true);
  }

  const closeModal = () => {
    setIsModalOpen(false);
  }

  async function enterAccount() {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/auth/reg/', {
        method: POST, 
        headers: {
          
        },
        body: {
          
        }
      });

      
    } catch {
      
    }
  }

  return (
    <>
      <div onClick={openModal} className='blue-btn-active join-account'>
          Вход и регистрация
      </div>

      {isModalOpen && (
        <>
          <div className="backdrop" onClick={closeModal}></div>
          <div className="modal">
            <div className="modal__snake-title-module">
              <div className="modal__snake-title-module__close" onClick={closeModal}>X</div>
              <h3 className="modal__snake-title-module__head">Вход</h3>
            </div>
            <div className="modal__snake-content-module">
              <form action="" className='modal__snake-form-module'>
                <div className="modal__snake-form-module__input_wrapper">
                  <p className='modal__snake-form-module__title'>Телефон или почта</p>
                  <input type="text" className='modal__snake-form-module__login-input' />
                  <p className='modal__snake-form-module__title'>Пароль</p>
                  <input type="text" className='modal__snake-form-module__login-input' />
                </div>
                <div className="modal__snake-form-module__enter-btn">
                  <button className='modal__snake-form-module__continue-btn' onClick={enterAccount}>Войти</button>
                </div>
              </form>
            </div>
          </div> 
        </>
      )}
    </>
  )
}
