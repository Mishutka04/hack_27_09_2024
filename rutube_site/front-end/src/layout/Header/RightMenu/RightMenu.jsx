import { ContentModule } from '@components/ContentModule/ContentModule';
import { Account } from '@components/Account/Account';
import { useMediaQuery } from 'react-responsive';

import lightSVG from '@assets/HeaderMenuIcons/light.svg';
import notificationSVG from '@assets/HeaderMenuIcons/notification.svg';
import plusSVG from '@assets/HeaderMenuIcons/plus.svg';
import searchSVG from '@assets/HeaderMenuIcons/search.svg'
import accountSVG from '@assets/HeaderMenuIcons/account.svg'

import './RightMenu.style.css';

export const RightMenu = () => {
  const isTablet = useMediaQuery({query: '(max-width: 1024px)'});

  return (
    <div className='header__right-menu'>
      <div className='header__right-menu__modules'>
        {isTablet ? <ContentModule svg={searchSVG}/> : ''}
        {isTablet ? '' : <ContentModule svg={plusSVG}/>}
        <ContentModule svg={notificationSVG}/>
        <ContentModule svg={lightSVG}/>
        {isTablet ? <ContentModule svg={accountSVG} color={'#1EABE9'} /> : ''}
      </div>
      {isTablet ? '' : <Account />}
    </div>
  )
}
