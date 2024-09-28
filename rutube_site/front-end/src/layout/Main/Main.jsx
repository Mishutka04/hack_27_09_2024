import { LeftSideMenu } from '@components/LeftSideMenu/LeftSideMenu';
import { MainContent } from './MainContent/MainContent';
import { useMediaQuery } from 'react-responsive';

import './Main.style.css';

// eslint-disable-next-line react/prop-types
export const Main = ({ isMenuOpen }) => {
  const isTablet = useMediaQuery({query: '(max-width:1024px)'});

  return (
    <main className='main'>
        {isTablet ? '' : <LeftSideMenu isMenuOpen={isMenuOpen} />}
        <MainContent />
    </main>
  )
}
