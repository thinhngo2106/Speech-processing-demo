import React, {useEffect, useState}  from 'react';
import { Link, Redirect, useParams} from 'react-router-dom';
import "./css/home.css";
import {Layout, Container, BoxUpload} from '../components/style'
import { useDispatch, useSelector } from 'react-redux';
import LoadingBox from '../components/LoadingBox';
import MessageBox from '../components/MessageBox';
import 'bootstrap/dist/css/bootstrap.min.css';
import CarouselContainer from '../components/CarouselContainer'
import Axios from 'axios';
import FolderIcon from './../assets/images/folder_icon_transparent.png';
import PacmanLoader from "react-spinners/PacmanLoader";
import { css } from "@emotion/react";
import Speech from 'react-speech';
import { GiSpeaker } from 'react-icons/gi';
export default function HomeScreen(props) {
    const [audio, setAudio] = useState('');
    const [music, setMusic] = useState(''); 

    const [check, setCheck] = useState('');
    const [nameMusic, setNameMusic] = useState('');
    const [loadingUpload, setLoadingUpload] = useState(false);
    const [errorUpload, setErrorUpload] = useState('');
    const [isUploaded, setIsUploaded] = useState(false);
    let [color, setColor] = useState("#3949ab");
    const dispatch = useDispatch();
    const override = css`
      display: block;
      margin-left: 130px !important;
      border-color: red;
    `;

    useEffect(()=>{
  
    }, dispatch, audio, music, check)

    const style = {
      play: {
        button: {
          width: '28',
          height: '28',
          cursor: 'pointer',
          pointerEvents: 'none',
          outline: 'none',
          backgroundColor: 'yellow',
          border: 'solid 1px rgba(255,255,255,1)',
          borderRadius: 6
        },
      }
    };


    const uploadFileHandler = async (e) => {
        const file = e.target.files[0]
        if (e.target.files[0] && e.target.files) {
          setNameMusic(file['name'])
          let reader = new FileReader()
          reader.onload= (e) => {
            setMusic(e.target.result)
           
            setIsUploaded(true);
          }
          reader.readAsDataURL(e.target.files[0])
        }
        const bodyFormData = new FormData();
        bodyFormData.append('file_audio', file);
        setLoadingUpload(true);
        try {
          const { data } = await Axios.post('/audio/', bodyFormData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          });

          console.log(data['class_name'])
          setAudio(data['class_name']);
          setLoadingUpload(false);
          
        } catch (error) {
          setErrorUpload(error.message);
          setLoadingUpload(false);
        }
      };

    const clickMe = async(e) =>{
        setNameMusic('')
        setAudio('')
        setMusic('')
        setIsUploaded(false)
        
    }

    return(
      <div className="main">
        <CarouselContainer/>
        <div className="layout">
        <Layout>
          <Container>
            <h2>Upload Your File</h2>
            <p>File should be mp3</p>
            <BoxUpload>
              <div className='add-audio'>
              {!isUploaded ? (
                 <>
                  <div>
                  <label htmlFor="imageFile">
                    <img
                      src={FolderIcon}
                      draggable={"false"}
                      alt="placeholder"
                      style={{ width: 100, height: 100 }}
                    />
                    <p style={{ color: "#444" }}>Click to upload folder</p>
                  </label>
                    <input
                      type="file"
                      name="file_audio"
                      id="imageFile"
                      label="Chọn ảnh"
                     onChange={uploadFileHandler}
                    ></input>
                    </div>
                     </>
                     ) : (
                    <div>
                    {music ? (
                      <div className= "audio_class">
                         
                        <div className= "audio_class">Name song: {nameMusic}</div>
                      <audio controls>
                        <source src = {music} type="audio/mpeg"/>
                      </audio> 
                      </div>
                    ):(
                      <div></div>
                    )}
                  
                    {audio ? (
                      <div className= "class_audio">
                        
                        <a>Music genre: {audio}</a>
                        <GiSpeaker>
                        <Speech text= {`music genre is: ${audio}`} 
                        voice="Google UK English Male"
                        >
                          
                        </Speech>
                        </GiSpeaker>
                      </div>                  
                    ) : (
                     <div></div>
                    )}
        
                      {loadingUpload && <PacmanLoader color={color} loading={loadingUpload} css={override} size={15} />}
                      {errorUpload && (
                      <MessageBox variant="danger">{errorUpload}</MessageBox>    
                    )}
                     <div className= "class_audio">
                          <button className="button" onClick={clickMe}>Quay lại</button>
                      </div>
                    </div>
                    )}
                  </div>
                </BoxUpload>
            </Container>
        </Layout>
        </div>
    </div>
    );

}