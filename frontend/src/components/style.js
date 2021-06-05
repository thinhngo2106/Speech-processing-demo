import styled from 'styled-components'

export const Layout = styled.div`
    height: 100%;
    width: 100%;
    display: grid;
    place-items: center;
    background: #F5F8FF;
    float: left;
`

export const Container = styled.div`
    display: flex;
    flex-direction: column;
    background: #fff;
    padding: 36px 48px;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
    border-radius: 20px;
    text-align: center;
    p {
        margin-top: -10px;
        color: #777;
    }
`

export const BoxUpload = styled.div`
    display: grid;
    margin-top: 20px;
    place-items: center;
    border: 1px dashed #799CD9;
    /* padding: 36px 48px; */
    position: relative;
    height: 350px;
    width: 350px;
    background: #FBFBFF;
    border-radius: 20px;
    .image-upload {
        display: flex;
        flex-wrap:wrap;
        label {
            cursor: pointer;
        
            :hover {
                opacity: .8;
            }
        }
        >input {
            display: none;
        }
    }
`