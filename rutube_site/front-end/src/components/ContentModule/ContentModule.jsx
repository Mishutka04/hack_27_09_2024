import './ContentModule.style.css';

// eslint-disable-next-line react/prop-types
export const ContentModule = ({svg, color='#29333D'}) => {
  return (
    <div className='content-module' style={{borderColor: color}}>
        <img src={svg} className='content-module__icon'/>
    </div>
  )
}