import React, { useState } from 'react';
import { GoogleLogout, GoogleLogin } from 'react-google-login';
import styled from 'styled-components';
import { Auth } from '../SearchWrapper';
import config from '../../config/ConfigLoader';

const CustomGoogleLogin = styled(GoogleLogin)`
    width: 100px;
    height: 56px;
    margin-top: auto;
    margin-bottom: auto;
    margin-right: 5px;
`;

const CustomGoogleLogout = styled(GoogleLogout)`
    width: 100px;
    height: 56px;
    margin-top: auto;
    margin-bottom: auto;
    margin-right: 5px;
`;

export interface GoogleButtonProps {
    setTokenID: (tokenID: Auth['tokenID']) => void;
}

interface State {
    isLoggedIn: boolean;
}

/*
    Button that handles google login and logout
*/
const GoogleButton: React.FC<GoogleButtonProps> = ({ setTokenID }) => {
    const [isLoggedIn, setIsLoggedIn] = useState<State['isLoggedIn']>(false);

    const logIn = (response) => {
        setTokenID(response.tokenObj.id_token);
        setIsLoggedIn(true);
    };

    const logOut = () => {
        setTokenID('');
        setIsLoggedIn(false);
    };

    const handleError = () => {};

    return (
        <>
            {!isLoggedIn && (
                <CustomGoogleLogin
                    clientId={config.clientId}
                    buttonText="Login"
                    onSuccess={logIn}
                    onFailure={handleError}
                    responseType="id_token"
                    cookiePolicy={'single_host_origin'}
                />
            )}
            {isLoggedIn && (
                <CustomGoogleLogout
                    clientId={config.clientId}
                    buttonText="Logout"
                    onLogoutSuccess={logOut}
                    onFailure={handleError}
                    cookiePolicy={'single_host_origin'}
                />
            )}
        </>
    );
};

export default GoogleButton;
