// Initial Stage
function init() {
  $("#user-details").show();
  $("#did-provisioning").hide();
  $("#select-plans").hide();
  $("#summaryReport").hide();
  $("#askingNeedDiDBulk").hide();
  $("#selectAll").hide();
}

init();

let showBulkFileUpload;

// Get User Form Details
let userDetails = {};

document
  .getElementById("userDetailsSubmit")
  .addEventListener("click", function () {
    let userFieldName,
      userValue,
      inputFiledName,
      userSubmittedValues = document.user_submmitted_details.elements;

    for (var i = 0; i < userSubmittedValues.length; i++) {
      userFieldName = userSubmittedValues[i].name;
      userValue = userSubmittedValues[i].value;
      inputFiledName = `input[name='${userFieldName}']`;
      if (userValue == "") {
        $(inputFiledName).addClass("border border-danger");
      } else {
        $(inputFiledName).removeClass("border border-danger");
        userDetails[`${userFieldName}`] = userValue;
      }
    }

    if (!$("#doYouNeedDIDCheckbox").is(":checked")) {
      $("#user-details").hide();
      $("#select-plans").show();
    } else {
      $("#user-details").hide();
      $("#did-provisioning").show();
    }

    userDetails.voiceMail =
      $("#voiceMail").prop("checked") == true ? true : false;

    document.getElementById("didCountryValue").value = userDetails.country;
    document.getElementById("didCountryValue").innerText = userDetails.country;

    document.getElementById("didStateValue").value = userDetails.stateProvince;
    document.getElementById("didStateValue").innerText =
      userDetails.stateProvince;

    document.getElementById("didCityValue").value = userDetails.city;
    document.getElementById("didCityValue").innerText = userDetails.city;
  });

// Get DID Number
let chooseDIDNumberDetails = {};

$("#selectAllBox").click(function () {
  $("#generateNumber input").prop("checked", $(this).prop("checked"));
});

document
  .getElementById("choose_did_provisioning")
  .addEventListener("click", function () {
    $("#purchase_number").removeClass("d-none");

    $("#selectAll").show();

    let chooseDIDfiledName,
      chooseDIDfiledValue,
      inputFiledName,
      chooseDIDNumber = document.choose_did_provisioning.elements;

    for (var i = 0; i < chooseDIDNumber.length; i++) {
      chooseDIDfiledName = chooseDIDNumber[i].name;
      chooseDIDfiledValue = chooseDIDNumber[i].value;
      inputFiledName = `input[name='${chooseDIDfiledName}']`;
      if (chooseDIDfiledValue == "") {
        $(inputFiledName).addClass("border border-danger");
      } else {
        $(inputFiledName).removeClass("border border-danger");
        chooseDIDNumberDetails[`${chooseDIDfiledName}`] = chooseDIDfiledValue;
      }
    }

    let dispalyNumberFormat = `${chooseDIDNumberDetails.didNumberFormat}-555-`;
    for (
      let length = 1;
      length <= chooseDIDNumberDetails.didNumberDisplayCount;
      length++
    ) {
      let finalFormatToDisplay = dispalyNumberFormat + (1000 + length);
      document.getElementById(
        "generateNumber"
      ).innerHTML += `<div style='width: 30%;border: 1px solid #b5bdca; padding: 5px; text-align:center; float:left;'><input type='checkbox' class='form-check-input' name='userChooseenDIDNumber' value="${finalFormatToDisplay}"> <label class='form-check-label'>${finalFormatToDisplay}</label></div>`;
    }
  });

// User Selected Numbers
let userPickedNumber = [];

document
  .getElementById("purchase_number")
  .addEventListener("click", function () {
    userPickedNumber = [];
    let didChoosen = document.querySelectorAll(
      "input[name=userChooseenDIDNumber]:checked"
    );

    for (let i = 0; i < didChoosen.length; i++) {
      userPickedNumber.push(didChoosen[i].value);
    }

    chooseDIDNumberDetails.userPickedNumber = userPickedNumber;
    $("#did-provisioning").hide();
    $("#select-plans").show();
    $("#askingNeedDiDBulk").show();
  });

// Estimating Plan
let activeServices = [],
  selectedServiceName = [];

function planPrice(name) {
  let servicePrice = 0,
    activeFiled = document.getElementsByName(name),
    planPrice = activeFiled,
    activeServices = [],
    selectedServiceName = [],
    profilePlanValue = 0,
    callingPlanValue = 0,
    numberOfUsers = document.getElementById("planNoOfUsers").value,
    activeServiceBox = document.querySelectorAll(
      "input[name=servicesCheckBox]:checked"
    ),
    finalProfilePrice = document.getElementById("profilePrice"),
    finalCallingPrice = document.getElementById("callingPrice"),
    finalServicePrice = document.getElementById("services");

  if (name == "planNoOfUsers") {
    document.getElementById("noOfUsers").innerText = numberOfUsers;
  }

  for (i = 0; i < planPrice.length; i++) {
    if (planPrice[i].checked) {
      if (name == "selectProfilePlan") {
        profilePlanValue = Number(planPrice[i].value);
        finalProfilePrice.innerText = planPrice[i].value;
      }

      if (name == "selectCallingPlan") {
        callingPlanValue = Number(planPrice[i].value);
        finalCallingPrice.innerText = planPrice[i].value;
      }
    }
  }

  for (let i = 0; i < activeServiceBox.length; i++) {
    activeServices.push(activeServiceBox[i].value);
    if (activeServiceBox[i].value == 1) {
      selectedServiceName.push(" E-911 ");
    }
    if (activeServiceBox[i].value == 2) {
      selectedServiceName.push(" RoboCall Blocking ");
    }
    if (activeServiceBox[i].value == 3) {
      selectedServiceName.push(" Teams Compliance Recording ");
    }
    if (activeServiceBox[i].value == 4) {
      selectedServiceName.push(" MS Teams Contact Center ");
    }
    if (activeServiceBox[i].value == 5) {
      selectedServiceName.push(" E-Fax Hosting ");
    }
    if (activeServiceBox[i].value == 6) {
      selectedServiceName.push(" Performance Analytics ");
    }
  }

  document.getElementById("summarySelectedServicesLables").innerText =
    selectedServiceName;

  for (let i = 0; i < activeServices.length; i++) {
    servicePrice += Number(activeServices[i]);
  }

  document.getElementById("services").innerText = activeServices.length;
  let finalEstimation =
    (Number(finalProfilePrice.innerText) +
      Number(finalCallingPrice.innerText) +
      Number(finalServicePrice.innerText)) *
    Number(numberOfUsers);
  document.getElementById("totalEstimation").innerText = finalEstimation;
}

// Plans Selection
let selectedPlans = {};
document
  .getElementById("chooseYourPlan")
  .addEventListener("click", function () {
    let selectPlanfiledName,
      selectPlanfiledValue,
      inputFiledName,
      selectPlanNumber = document.chooseYourPlan.elements;

    document.querySelectorAll("input[name=phoneNum]:checked");

    for (var i = 0; i < selectPlanNumber.length; i++) {
      selectPlanfiledName = selectPlanNumber[i].name;
      selectPlanfiledValue = selectPlanNumber[i].value;
      inputFiledName = `input[name='${selectPlanfiledName}']`;
      if (selectPlanfiledValue == "") {
        $(inputFiledName).addClass("border border-danger");
      } else {
        $(inputFiledName).removeClass("border border-danger");
        if (selectPlanNumber[i].checked) {
          selectedPlans[`${selectPlanfiledName}`] = selectPlanfiledValue;
        }
      }
    }

    generateSummary();
  });

// Generate Summary
function generateSummary() {
  $("#select-plans").hide();
  $("#summaryReport").show();
  // User Details

  document.getElementById("userregion").innerText = userDetails.userRegion;
  document.getElementById("usercompanyName").innerText =
    userDetails.companyName;
  document.getElementById("userFirstName").innerText = userDetails.firstName;
  document.getElementById("userlastName").innerText = userDetails.lastName;
  document.getElementById("useremailId").innerText = userDetails.email;
  document.getElementById("uservoiceMail").innerText = userDetails.voiceMail;
  document.getElementById("userstreetAddress1").innerText =
    userDetails.streetAddressOne;
  document.getElementById("userstreetAddress2").innerText =
    userDetails.streetAddressTwo;
  document.getElementById("usercity").innerText = userDetails.city;
  document.getElementById("userstate").innerText = userDetails.stateProvince;
  document.getElementById("userpostalcode").innerText = userDetails.postelCode;
  document.getElementById("usercountry").innerText = userDetails.country;
  document.getElementById("userProjectName").innerText =
    userDetails.projectName;
  document.getElementById("userDealStatus").innerText = userDetails.dealStatus;
  document.getElementById("userProjectNotes").innerText =
    userDetails.projectNotes;
  if (userDetails.doYouHaveDID == "No") {
    document.getElementById("pickedNumbers").innerText =
      userDetails.enteredDidNumber;
  } else {
    console.log(chooseDIDNumberDetails.userPickedNumber.length);
    if (chooseDIDNumberDetails.userPickedNumber.length > 1) {
      document.getElementById("pickedNumbers").innerText =
        chooseDIDNumberDetails.userPickedNumber[0] +
        " to " +
        chooseDIDNumberDetails.userPickedNumber[
          chooseDIDNumberDetails.userPickedNumber.length - 1
        ];
    } else {
      document.getElementById("pickedNumbers").innerText =
        chooseDIDNumberDetails.userPickedNumber;
    }
  }

  // Plan Details
  document.getElementById("summaryProfilePrice").innerText =
    "$" + document.getElementById("profilePrice").innerText;
  document.getElementById("summaryNoOfusers").innerText =
    document.getElementById("noOfUsers").innerText;
  document.getElementById("summaryCallingPlan").innerText =
    "$" + document.getElementById("callingPrice").innerText;
  document.getElementById("summarySelectedServices").innerText =
    "$" + document.getElementById("services").innerText;
  document.getElementById("summarytotalEstimation").innerText =
    "$" + document.getElementById("totalEstimation").innerText;

  if (document.getElementById("summaryProfilePrice").innerText == 4) {
    document.getElementById("summaryProfilePriceLable").innerText =
      "Silver Profile";
  } else {
    document.getElementById("summaryProfilePriceLable").innerText =
      "Gold Profile";
  }

  if (document.getElementById("summaryCallingPlan").innerText == 10) {
    document.getElementById("summaryCallingPlanLable").innerText =
      "Metered National and International (Per mnute rates apply)";
  } else {
    document.getElementById("summaryCallingPlanLable").innerText =
      "Unlimited National (Metered International)";
  }

  document.getElementById("userdidNumber").innerText = $(
    "#doYouNeedDIDCheckbox"
  ).is(":checked");
  document.getElementById("uPrimaryNumber").innerText =
    userDetails.primaryNumber;
}
