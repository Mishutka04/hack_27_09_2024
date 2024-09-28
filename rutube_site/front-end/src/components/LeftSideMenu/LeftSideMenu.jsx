import { ListMenuItem } from '@components/ListMenuItem/ListMenuItem'; 

import './LeftSideMenu.style.css';

import homeSVG from '@assets/LeftSideMenuIcons/home.svg';
import catalogSVG from '@assets/LeftSideMenuIcons/catalog.svg';
import botSVG from '@assets/LeftSideMenuIcons/bot.svg';

// eslint-disable-next-line react/prop-types
export const LeftSideMenu = ({ isMenuOpen }) => {
  return (
    <nav className={`main__left-side-menu ${isMenuOpen ? 'opened' : 'closed'}`}>
      <ul className={`main__left-side-menu__list-group ${isMenuOpen ? 'opened' : 'closed'}`}>
        <ListMenuItem svg={homeSVG} text={'Главная'} isOpened={isMenuOpen ? true : false} />
        <ListMenuItem svg={catalogSVG} text={'Каталог'} isOpened={isMenuOpen ? true : false} />
        <ListMenuItem svg={botSVG} text={'Ответ-бот'} isOpened={isMenuOpen ? true : false} />
      </ul>
    </nav>
  )
}
