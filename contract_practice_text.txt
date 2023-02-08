// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.5.0;

contract TrialLog {
    uint DateOfEntry;
    string UserID = "UserID";
    string group = "Control or Test";
    uint DOB;
    string sex = "M or F";
    bool Consent;
    uint ZipCode;
    string ClinicIdentifier = "Clinic Identifier";
    uint TrialPhase;
    uint BloodPressure;
    uint BodyTemp;
    bool Fasting;
    string MedAdministered = "Medication Administered";
    bool HasSymptoms;
    string result = "Result";


    function updateLog(uint newDateOfEntry, string memory newUserID, string memory newgroup, uint newDOB, string memory newsex, bool newConsent, uint newZipCode, string memory NewClinicIdentifier, uint newTrialPhase, uint newBloodPressure, uint newBodyTemp, bool newFasting, string memory newMedAdministered, bool newHasSymptoms, string memory newresult) public {
       DateOfEntry = newDateOfEntry;
       UserID = newUserID;
       group = newgroup;
       DOB = newDOB;
       sex = newsex;
       Consent = newConsent; // Did they fulfill the consent agreement Y/N?
       ZipCode = newZipCode;
       ClinicIdentifier = NewClinicIdentifier;
       TrialPhase = newTrialPhase;
       BloodPressure = newBloodPressure;
       BodyTemp = newBodyTemp;
       Fasting = newFasting;
       MedAdministered = newMedAdministered;
       HasSymptoms = newHasSymptoms;
       result = newresult;
   }
}