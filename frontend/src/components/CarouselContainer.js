import React from 'react';
import { Carousel } from 'react-bootstrap';
import image1 from './../assets/images/image1.png';
import image2 from './../assets/images/image2.png';
import image3 from './../assets/images/image3.png';
import './slide.css'

const CarouselContainer = () => {
  return (
    <Carousel fade={true} pause={false} className ="carousel">
      <Carousel.Item interval={2000}>
        <img
          className="d-block image"
          src={image1}
        

          alt="First slide"
        />
        <Carousel.Caption>
          <h3>First slide label</h3>
          <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item interval={2000}>
        <img
          className="d-block image"
          src={image2}

          alt="Third slide"
        />
        <Carousel.Caption>
          <h3>Second slide label</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item interval={2000}>
        <img
          className="d-block image"
          src={image3}
         
          alt="Third slide"
        />
        <Carousel.Caption>
          <h3>Third slide label</h3>
          <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  )
}

export default CarouselContainer;