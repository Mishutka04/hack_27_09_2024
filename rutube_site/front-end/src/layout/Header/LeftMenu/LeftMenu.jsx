import { Logo } from '@components/Logo/Logo.jsx';
import { BurgerMenu } from '@components/BurgerMenu/BurgerMenu.jsx'; 

import './LeftMenu.style.css';

// eslint-disable-next-line react/prop-types
export const LeftMenu = ({ toggleMenu }) => {
  return (
    <div className='header__left-menu'>
        <BurgerMenu toggleMenu={toggleMenu}/>
        <section className='header__left-menu__wrapper-logo'>
          <Logo />
        </section>
    </div>
  )
}
