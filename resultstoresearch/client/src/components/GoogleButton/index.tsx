// BackButton Component
/**
 * Component that handles user login / logout via google sign-in
 * @packageDocumentation
 */
import React, { useState, useContext } from 'react';
import { GoogleLogout, GoogleLogin } from 'react-google-login';
import styled from 'styled-components';
import config from '../../config/ConfigLoader';
import { AuthContext } from '../../contexts/AuthContext';

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

/** GoogleButton State */
interface State {
    /** True if user is logged in*/
    isLoggedIn: boolean;
}

/*
    Button that handles google login and logout
*/
export const GoogleButton: React.FC = () => {
    const authContext = useContext(AuthContext);
    const [isLoggedIn, setIsLoggedIn] = useState<State['isLoggedIn']>(false);

    const logIn = (response) => {
        authContext.setTokenId(response.tokenObj.id_token);
        setIsLoggedIn(true);
    };

    const logOut = () => {
        authContext.setTokenId('');
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
                    isSignedIn={true}
                />
            )}
            {isLoggedIn && (
                <CustomGoogleLogout
                    clientId={config.clientId}
                    buttonText="Logout"
                    onLogoutSuccess={logOut}
                    onFailure={handleError}
                    cookiePolicy={'single_host_origin'}
                    isSignedIn={true}
                />
            )}
        </>
    );
};

export default GoogleButton;
